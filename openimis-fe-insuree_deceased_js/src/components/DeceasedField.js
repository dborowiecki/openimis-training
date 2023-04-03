import React, { useEffect, useState } from "react";
import { useModulesManager, useTranslations } from "@openimis/fe-core";
import {
  PublishedComponent,
} from "@openimis/fe-core";

import { useInsureeDeceasedQuery } from "../hooks";

const InsureeDeceasedField = (props) => {
  const {
    edited,
    readOnly,
    updateAttribute
  } = props;

  const updateEdited = (v) => {
    console.log("Edited jsonExt: ", edited.jsonExt)
     if (!!edited.jsonExt) {
      updateAttribute('jsonExt', {...edited.jsonExt, 'deceaseDate': v})
     } else {
      updateAttribute('jsonExt', { 'insureeDeceased':  {'deceaseDate': v}})
     }

  }

  let value;
  if (!!edited.uuid) {
    let filters = {insuree_Uuid: edited.uuid}
    const { isLoading, error, data } = useInsureeDeceasedQuery({filters})
    const editedValue = edited?.jsonExt?.insureeDeceased
    value = editedValue ? editedValue.deceaseDate : data?.deceaseDate
  } else {
    const editedValue = edited?.jsonExt?.insureeDeceased
    value = editedValue ? editedValue.deceaseDate : null
  }
  return (
    <PublishedComponent
      pubRef="core.DatePicker"
      value={value}
      module="insureeDeceased"
      label="Insuree.deceaseDate"
      readOnly={readOnly}
      required={false}
      onChange={(v) => updateEdited(v)}
    />
  );
};

export default InsureeDeceasedField;
