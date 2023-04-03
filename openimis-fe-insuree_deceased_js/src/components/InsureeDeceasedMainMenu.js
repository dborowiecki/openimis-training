import React, { Component } from "react";
import { useDispatch, useSelector } from "react-redux";
import { AssignmentInd, Person } from "@material-ui/icons";

import { MainMenuContribution, useTranslations, useModulesManager } from "@openimis/fe-core";
import { MenuItem } from "@material-ui/core";
import ListItemText from "@material-ui/core/ListItemText";
import { RIGHT_INSUREE } from "../constants";

const INSUREE_MAIN_MENU_CONTRIBUTION_KEY = "insuree_deceased.MainMenu";

const InsureeDeceasedMainMenu = (props) => {
  console.log("Insuree Deceased reached")
  const modulesManager = useModulesManager();
  const { formatMessage } = useTranslations("insuree_deceased", modulesManager);

  const rights = useSelector((state) => state.core?.user?.i_user?.rights ?? []);
  
  const handleMenuSelect = ( route) => {
    // block normal href only for left click
    this.redirect(route);
  };

  let entries = [];
  // if (rights.includes(RIGHT_INSUREE)) {
    entries.push({
      text: formatMessage("menu.Deceased"),
      icon: <Person />,
      route: "/insuree_deceased/registration",
    });
  // }


  //if (!entries.length) return null;
  return (
    //"Extension for insuree deceased."
    <MenuItem onClick={(e) => this.handleMenuSelect("/insuree_deceased/registration")} 
      component="a"  href={`${process.env.PUBLIC_URL || ""}/insuree_deceased/registration`} passHref>
         <ListItemText primary="Registry"/>                  
    </MenuItem>
  );
}

export default InsureeDeceasedMainMenu;
