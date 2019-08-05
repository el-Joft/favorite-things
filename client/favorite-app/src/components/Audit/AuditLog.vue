<template>
  <div>
    <md-table md-card>
      <md-table-toolbar>
        <h1 class="md-title">Favorite</h1>
      </md-table-toolbar>

      <md-table-row>
        <md-table-head>Task</md-table-head>
        <md-table-head>Performed(New/old)</md-table-head>
        <md-table-head>Action</md-table-head>
        <md-table-head>Date</md-table-head>
      </md-table-row>

      <md-table-row v-for="audit in audits" :key="audit.id">
        <md-table-cell>{{ audit.tableName }}</md-table-cell>
        <md-table-cell>
          <div class="container">
            <div class="row" v-if="Object.keys(JSON.parse(audit.tableFields)).length > 0">
              <div class="col-md-6">
                <div>
                  <p><strong>Title: </strong>{{ JSON.parse(audit.tableFields).title || JSON.parse(audit.tableFields).new.title }}</p>
                  <p><strong>Description: </strong>{{ JSON.parse(audit.tableFields).description || JSON.parse(audit.tableFields).new.description }}</p>
                  <p><strong>Ranking: </strong>{{ JSON.parse(audit.tableFields).ranking || JSON.parse(audit.tableFields).new.ranking }}</p>
                </div>
              </div>
              <div class="col-md-6">
                <div>
                  <p>{{ JSON.parse(audit.tableFields).title || JSON.parse(audit.tableFields).old.title }}</p>
                  <p>{{ JSON.parse(audit.tableFields).description || JSON.parse(audit.tableFields).old.description }}</p>
                  <p>{{ JSON.parse(audit.tableFields).ranking || JSON.parse(audit.tableFields).old.ranking }}</p>
                </div>
              </div>
            </div>
          </div>
        </md-table-cell>
        <md-table-cell>{{ audit.action }}</md-table-cell>
        <md-table-cell>{{audit.timestamp}}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
import {
  AUDIT_LOG
} from '@/graphql'
export default {
  name: 'auditLog',
  data () {
    return {
      audits: [],
      tableData: {}
    }
  },
  apollo: {
    audits: {
      query: AUDIT_LOG
    }
  },
  methods: {
    jsonObject (tableFields) {
      const temp = JSON.parse(tableFields)
      if (temp.new) {
        this.tableData = temp.new
      } else {
        this.tableData = temp
      }
    }
  }
}
</script>

<style>
  .md-title {
    text-align: center;
    padding: 40px 0;
    font-family: 'Capriola', sans-serif;
  }
</style>
