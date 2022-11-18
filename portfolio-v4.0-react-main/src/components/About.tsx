import Image from './Image';
import resume from "../assets/pdf/resume.pdf";
const aboutStyle = {
    transition: 'all 2s',
    padding: '40vh 10px 0vh 10px',
    maxWidth: '650px',
    marginLeft: '35px'
  
}

type Props = {
    windowWidth: number
}

export default function About({ windowWidth }: Props) {
    return (
        <section style={aboutStyle}>
            <div id="about">
                <Image src="photo.jpg"  isHidden={false} />
            </div>
            <p>
            My name is Mondoa Nelson, I am a Data Analyst and live in Warsaw, Poland. I extract, analyze and visualize data in order to provide constructive predictions, beneficial to any business organisation.
           </p>
          
            <p>
            All of the projects listed below are 100% my own work, with the exception of collaborations, which are clearly marked with the collaborators credited on my GitHub page.
            </p>
            <div style={{display: 'flex', justifyContent: windowWidth < 500 ? 'center' : 'flex-start'}}>
                <a href="https://github.com/njimonda" target="_blank" rel="noopener noreferrer">Visit my GitHub</a>
                <a href={resume} target="_blank" rel="noopener noreferrer">See my Resume</a>
            </div>
        </section>
    );
  }