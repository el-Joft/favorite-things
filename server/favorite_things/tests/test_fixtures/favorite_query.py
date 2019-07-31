create_favorite_query = '''
mutation {{
  createFavorite (
    title: "{title}",
    description: "{description}",
    category: "{category}",
    ranking: {ranking}
  ) {{
    message
    errors
    favorite {{
      id
      title
    }}
  }}
}}
'''

update_favorite_query = '''
mutation {{
  updateFavorite (
    id: "{id}",
    title: "{title}",
    description: "{description}",
    category: "{category}",
    ranking: {ranking}
  ) {{
    message
    errors
    favorite {{
      id
      title
      description
      ranking
      category {{
        id
        name
      }}
    }}
  }}
}}
'''

delete_favorite_query = '''
mutation {{
  deleteFavorite(
    id: "{id}"
  ) {{
    message
    favorite {{
      title
    }}
  }}
}}
'''

all_favorites = '''
query {
  favorites {
    id
    ranking
    title
    category {
      id
      name
    }
  }
}
'''

single_favorite = '''
query {{
  favorite(id: "{id}") {{
    id
    title
    description
    category {{
      id
      name
    }}
  }}
}}
'''

all_audit_log = '''
query {
  audits {
    id
    tableName
    tableFields
    timestamp
    action
  }
}
'''
