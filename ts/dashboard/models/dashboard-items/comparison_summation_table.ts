module ts {
  export module models {

    /**
     * A summation table that compares two arbitrary queries.
     */
    export class ComparisonSummationTable extends TablePresentation {
      static meta: DashboardItemMetadata = {
        icon: 'fa fa-table',
        category: 'data-table',
        requires_data: true
      }

      private _query_other: string

      constructor(data?: any) {
        super(data)
        if (data) {
          if (this.query_other instanceof ts.models.data.Query) {
            this._query_other = data.query_other.name
          } else {
            this._query_other = data.query_other
          }
        }
        this._update_query()
      }

      _update_query() : void {
        if (this._query && this.query_other && this.dashboard) {
          let query = this.dashboard.definition.queries[this._query]
          this.query_override =
            query.join(this.query_other).set_name(this.item_id + '_joined')
          this.query_override.render_templates(ds.context().variables)
        }
      }

      get query_other() : ts.models.data.Query {
        if (!this.dashboard) {
          return null
        }
        return this.dashboard.definition.queries[this._query_other]
      }

      set query_other(value: ts.models.data.Query) {
        this._query_other = value.name
        this._update_query()
      }

      toJSON() : any {
        return $.extend(super.toJSON(), {
          query_other: this._query_other
        })
      }

      render() : string {
        this._update_query()
        return super.render()
      }

      data_handler(query: ts.models.data.Query) : void {
        var body = $('#' + this.item_id + ' tbody')
        var now  = query.data[0].summation
        var then = query.data[1].summation
        var diff = new ts.models.data.Summation(now).subtract(then)
        var properties = ['mean', 'min', 'max', 'sum']
        var float_margin = 0.000001
        properties.forEach((prop) => {
          var value = diff[prop]

          if (value > float_margin)
            diff[prop + '_class'] = 'ds-diff-plus'
          else if (value < -float_margin)
            diff[prop + '_class'] = 'ds-diff-minus'

          if ((float_margin > value) && (value > -float_margin))
            value = 0.0

          var pct = (now[prop] / then[prop]) - 1
          pct = isNaN(pct) ? 0.0 : pct
          diff[prop + '_pct'] = d3.format(',.2%')(Math.abs(pct))
          diff[prop] = Math.abs(value)
        })
        body.empty()
        body.append(ds.templates.models.comparison_summation_table_body({
          now:  now,
          then: then,
          diff: diff,
          item: this
        }))
        if (this.sortable) {
          body.parent().DataTable({
            autoWidth: false,
            paging: false,
            searching: false,
            info: false
          })
        }
      }

      interactive_properties(): PropertyListEntry [] {
        return super.interactive_properties().concat([
          {
            name: 'query_other',
            category: 'base',
            template: '{{item.query_other.name}}',
            edit_options: {
              type: 'select',
              source: function() {
                var queries = ds.manager.current.dashboard.definition.queries
                return Object.keys(queries).map(function(k) {
                  return { value: k, text: k }
                })
              },
              value: function(item) {
                return item.query_other ? item.query_other.name : undefined
              }
            }
          }
        ])
      }
    }
    ts.models.register_dashboard_item(ComparisonSummationTable)
  }
}
