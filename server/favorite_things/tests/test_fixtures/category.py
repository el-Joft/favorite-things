create_category_query = '''
mutation {{
  createCategory(name: "{name}") {{
    message
    errors
    category {{
      id
      name
    }}
  }}
}}
'''

all_category = '''
query {
  categories {
    id
    name
  }
}
'''

single_category = '''
query {{
  category(id: "{id}") {{
    id
    name
    favorite {{
      id
      ranking
    }}
  }}
}}
'''
