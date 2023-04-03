import { useModulesManager, useGraphqlQuery, useGraphqlMutation } from "@openimis/fe-core";
import { useMemo } from "react";
import _ from "lodash";

export const useInsureeDeceasedQuery = ({ filters }, config) => {
    const modulesManager = useModulesManager();
    console.log("FITLERS", filters)
    const { isLoading, error, data, refetch } = useGraphqlQuery(
      `
      query (
        $insuree_Uuid: String
        ) {
        insureeDeceased (insuree_Uuid:$insuree_Uuid) {
          edges {
            node {
              deceaseDate
            }
          }
        }
      }
    `,
      filters,
      config,
    );
  
    const deceased = useMemo(() => (data ? _.map(data.insureeDeceased?.edges, "node") : []), [data]);

    return { isLoading, error, data: deceased[0], refetch };
  };