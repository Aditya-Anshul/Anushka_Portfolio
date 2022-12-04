import clo from "../media/clovirtualfashion_logo_1486533344.jpg";
import illustrator from "../media/adobe-illustrator-icon.svg";
import draw from "../media/draw-icon.png";
import loom from "../media/loom.png";
import photoshop from "../media/adobe-photoshop-icon.svg";
import lightroom from "../media/adobe-lightroom-icon.png";
import canva from "../media/Canva-app-logo.png";

export const skillsImage = (skill) => {
  const skillID = skill.toLowerCase();
  switch (skillID) {
    case "clo":
      return clo;
    case "illustrator":
      return illustrator;
    case "draw":
      return draw;
    case "loom":
      return loom;
    case "photoshop":
      return photoshop;
    case "lightroom":
      return lightroom;  
    case "canva":
      return canva; 
    default:
      break;
  }
};
