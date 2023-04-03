import React from "react";
import { Checkbox, FormControlLabel } from "@material-ui/core";
import {
  useTranslations,
  useModulesManager,
} from "@openimis/fe-core";
import { injectIntl } from "react-intl";

const InsureeDeceasedFilter = (props) => {
  const {
    filters, onChangeFilters, intl
  } = props;

  const modulesManager = useModulesManager();
  const { formatMessage } = useTranslations("insuree_deceased", modulesManager);

  console.log("FILTERS: ", filters, filters?.additionalFilters?.value.insureeDeceased, filters?.additionalFilters?.insureeDeceased || false)
  const checked = filters?.additionalFilters?.value.insureeDeceased || false
  const updateFilters = (v) => {
    let value = filters?.additionalFilters?.value
    value = value ? {...value, 'insureeDeceased': v} : {'insureeDeceased': v}
    console.log(v)
    let f = `additionalFilters: "${JSON.stringify(value).replaceAll('\\"', "").replaceAll('"', '\\"')}"`
    onChangeFilters([
      {
        id: "additionalFilters",
        value: value,
        filter: v ? f : null}
    ])
  }

  return (
    <FormControlLabel
      control={
        <Checkbox
          color="primary"
          checked={checked}
          onChange={(e) => updateFilters(!checked)}
        />
      }
      label={formatMessage("Insuree.deceaseDate")}
    />
  );
};

export default InsureeDeceasedFilter;
