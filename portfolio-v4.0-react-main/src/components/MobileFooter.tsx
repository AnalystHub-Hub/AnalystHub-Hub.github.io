
const sectionStyle = {
    margin: '10px'
}

export default function MobileFooter() {

    return (
        <section id="contact" style={sectionStyle}>
            <div>
                        
                <div style={{display: 'flex', flexDirection: 'column', width: '100%'}}>
                    <a href="https://github.com/njimonda" target="_blank" rel="noopener noreferrer" className="bi bi-github">
                        <span style={{fontSize: '1em'}}> &nbsp; Check out some of my work on GitHub.</span> 
                    </a>
                    <a href="https://twitter.com/njimonda" target="_blank" rel="noopener noreferrer" className="bi bi-twitter">
                        <span style={{fontSize: '1em'}}> &nbsp; @njimonda on Twitter.</span> 
                    </a>
                    <a href="https://www.linkedin.com/in/nelson-m-99777b236/" target="_blank" rel="noopener noreferrer" className="bi bi-linkedin">
                        <span style={{fontSize: '1em'}}> &nbsp; Connect with me on Linkedin.</span> 
                    </a>
                    <a href="mailto:njiemondoa@gmail.com" className="bi bi-envelope">
                    <span style={{fontSize: '1em'}}> &nbsp; njiemondoa@gmail.com</span> 
                    </a>

                </div>
                <div style={{fontSize: '1em', display: 'flex', flexDirection: 'column', justifyContent: 'center', textAlign: 'center'}}>
                  <p>© Mondoa Nelson 2022.</p>
                </div>
                
            </div>
        </section>
      );
    }