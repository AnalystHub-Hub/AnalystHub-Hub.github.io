import { Link } from "react-scroll";
import resume from "../assets/pdf/resume.pdf";

type Props = {
  windowHeight: number
}

const navStyle: object = {
  position: 'absolute',
  padding: '10px',
  right: 0
}

const regular = {
  marginRight: '10px',
  cursor: 'pointer'
}

export default function Nav({windowHeight}: Props) {
    
    return (

        <nav style={navStyle}>
          <code>
            <Link
              style={regular}
              activeClass="active"
              to="about"
              spy={true}
              smooth={true}
              offset={windowHeight/-4}
              duration={500}
            ><span className="accent">./</span>About</Link>
            <Link
              style={regular}
              activeClass="active"
              to="projects"
              spy={true}
              smooth={true}
              offset={windowHeight/-4}
              duration={500}
            ><span className="accent">./</span>Projects</Link>
            <Link
              style={regular}
              activeClass="active"
              to="contact"
              spy={true}
              smooth={true}
              duration={1500}
            ><span className="accent">./</span>Contact</Link>
            <a style={regular} href={resume} target="_blank" rel="noopener noreferrer"><span className="accent">./</span>Resume</a>
          </code>   
      </nav>
    );
  }
  