import React, { useContext, useState } from "react";
import { Helmet } from "react-helmet";
import { Grid } from "@material-ui/core";
import { Link } from "react-router-dom";

const linkToPPTFile =
  "https://scholar.harvard.edu/files/torman_personal/files/samplepptx.pptx";

function ResourcePage() {
  return (
    <>
      <iframe
        src={`https://view.officeapps.live.com/op/embed.aspx?src=${linkToPPTFile}`}
        width="100%"
        height="600px"
        frameBorder="0"
        title="slides"
      ></iframe>
    </>
  );
}

export default ResourcePage;