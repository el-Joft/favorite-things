import gql from 'graphql-tag'

export const CREATE_FAVORITE_MUTATION = gql`mutation CreateFavoriteMutation($title: String!, $description: String, $metadata: [JSONString], $category: String!, $ranking: Int!) {
        createFavorite(
            title: $title,
            description: $description,
            metadata: $metadata,
            category: $category,
            ranking: $ranking
        ) {
            message
            errors
            favorite {
              id
              title
              description
              ranking
            }
            category {
              id
              name
            }
        }
    }`

export const ALL_FAVORITE_QUERY = gql`query allFavoriteQuery{
  favorites {
    id
    ranking
    title
    description
    category {
      id
      name
    }
  }
}`

export const ALL_CATEGORIES = gql`query allCategoryQuery{
  categories {
    id
    name
    favorite {
      id
      title
    }
  }
}`

export const AUDIT_LOG = gql`query allCategoryQuery{
  audits {
    id
    tableName
    tableFields
    timestamp
    action
  }
}`

export const SINGLE_CATEGORY = gql` query singleCategoryQuery($id: String!){
  category(id: $id) {
    id
    name
    favorite {
      id
      title
      description
      createdAt
      ranking
    }
  }
}`

export const SINGLE_FAVORITE = gql` query singleFavoriteQuery($id: String!){
  favorite(id: $id) {
      id
      title
      description
      createdAt
      ranking
      metadataSet {
      id
      key
      value
    }
      category {
      id
      name
    }
  }
}`

export const CREATE_CATEGORY_MUTATION = gql`mutation CreateCategoryMutation($name: String!) {
  createCategory(name: $name) {
    message
    errors
    category {
      id
      name
    }
  }
    }`

export const UPDATE_FAVORITE_MUTATION = gql`mutation CreateFavoriteMutation($id:String!, $title: String, $description: String, $category: String, $ranking: Int) {
   updateFavorite (
    id: $id,
    title: $title,
    description: $description,
    category: $category,
    ranking: $ranking
  ) {
    message
    errors
    favorite {
      id
      title
      description
      ranking
      category {
        id
        name
      }
    }
  }
}`

export const DELETE_FAVORITE_MUTATION = gql`mutation CreateCategoryMutation($id: String!) {
  deleteFavorite(
    id: $id
  ) {
    message
    favorite {
      id
      title
      description
      ranking
      category {
        id
        name
      }
    }
  }
}`
