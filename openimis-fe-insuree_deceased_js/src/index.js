import messages_en from "./translations/en.json";

import InsureeDeceasedField from "./components/DeceasedField";
import InsureeDeceasedFilter from "./components/DeceasedFilter";
import InsureeDeceasedMainMenu from "./components/InsureeDeceasedMainMenu"
import DeceasedInsureesReport from "./reports/DeceasedInsureesReport";



const DEFAULT_CONFIG = {
  "translations": [{ key: "en", messages: messages_en }],
  "insuree.Insuree": [InsureeDeceasedField],
  "insuree.Filter": [InsureeDeceasedFilter],
  "core.MainMenu": [InsureeDeceasedMainMenu],
  "core.LoginPage": [InsureeDeceasedMainMenu],
  "reports": [
    {
      key: "deceased_insurees_report",
      component: DeceasedInsureesReport,
      isValid: (values) => values.dateFrom && values.dateTo,
      getParams: (values) => ({
        dateFrom: values.dateFrom,
        dateTo: values.dateTo,
      }),
    }
  ]
}

export const InsureeDeceasedModule = (cfg) => {
  return { ...DEFAULT_CONFIG, ...cfg };
}