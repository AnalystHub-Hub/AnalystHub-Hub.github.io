
/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useState, useRef, MutableRefObject } from "react";
import Header from './components/Header';
import Footer from './components/Footer';
import MobileFooter from './components/MobileFooter';
import Left from './components/Left';
import Right from './components/Right';
import Intro from './components/Intro';
import Projects from './components/Projects';
import About from './components/About';


function App() {
  const introRef = useRef() as MutableRefObject<HTMLDivElement>;
  const aboutRef = useRef() as MutableRefObject<HTMLDivElement>;
  const projectsRef = useRef() as MutableRefObject<HTMLDivElement>;
  const footerRef = useRef() as MutableRefObject<HTMLDivElement>;

  const [initialHeaderShow, setInitialHeaderShow] = useState<boolean>(false);
  const [scrollPosition, setScrollPosition] = useState<number>(0);
  const [windowHeight, setWindowHeight] = useState<number>(0);
  const [windowWidth, setWindowWidth] = useState<number>(0);
  const [furthestDown, setFurthestDown] = useState<number>(0);
  const [headerHidden, setHeaderHidden] = useState<boolean>(true);  
  const [aboutOffset, setAboutOffest] = useState<number>(0);
  const [projectsOffset, setProjectOffset] = useState<number>(0);
  const [footerOffset, setFooterOffset] = useState<number>(0);
  const [footerExpand, setFooterExpand] = useState<boolean>(false);
  const [introHidden, setIntroHidden] = useState<boolean>(true);  
  const [aboutHidden, setAboutHidden] = useState<boolean>(true);
  const [onScreenProject, setOnScreenProject] = useState<string>("");


  const handleScroll = () => {
    setScrollPosition(window.pageYOffset);
    setAboutOffest(aboutRef.current.getBoundingClientRect().top);
    setProjectOffset(projectsRef.current.getBoundingClientRect().top);
    setFooterOffset(footerRef.current.getBoundingClientRect().top);
  };


  const handleResize = () => {
    setWindowHeight(window.innerHeight);
    setWindowWidth(window.innerWidth);
  };
  const handleRightNav = () => {
    if(scrollPosition > 200 && scrollPosition > furthestDown) {
      setFurthestDown(scrollPosition);
      if (initialHeaderShow) setHeaderHidden(true);
    } 
    if(scrollPosition < furthestDown-100) {
        setFurthestDown(scrollPosition);
        setHeaderHidden(false); 
    } 
    if (aboutOffset < 100 && !introHidden) {
      setIntroHidden(true);
    } 
    if (aboutOffset >= 300 && introHidden) {
      setIntroHidden(false);
    } 
    if (projectsOffset < 100 && !aboutHidden) {
      setAboutHidden(true);
    }
    if (projectsOffset >= 300 && aboutHidden) {
      setAboutHidden(false);
    }
    if (footerOffset <= windowHeight-50 && !footerExpand) {
      setFooterExpand(true);
    }
    if (footerOffset >= windowHeight+150 && footerExpand) {
      setFooterExpand(false);
    }
  }

  useEffect(() => {
    handleRightNav();
    
  }, [scrollPosition]);

  useEffect(() => {
    
    window.addEventListener("resize", handleResize);
    handleResize();
    handleScroll();
    setTimeout(() => {
      window.scrollTo(0, 0);
      setIntroHidden(false);
      setAboutHidden(false);

    }, 100);
    setTimeout(() => {
      setInitialHeaderShow(true);
      setHeaderHidden(false);
      window.addEventListener("scroll", handleScroll);  
    }, 1000);

    return () => {
      window.removeEventListener("scroll", handleScroll);
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  

  return (
    <div className="App">
      
        <Header hidden={headerHidden} scrollPosition={scrollPosition} windowHeight={windowHeight} windowWidth={windowWidth}/>

        { windowWidth < 940 ? <></> :
          <div id="top" className="noMobile">
            <Left scrollPosition={scrollPosition} footerExpand={footerExpand} />
   
            <Right windowHeight={windowHeight} introHidden={introHidden} aboutHidden={aboutHidden} onScreenProject={onScreenProject} />
          </div>
        }
        
        <main>
          
          <div ref={introRef} >
            <Intro windowWidth={windowWidth} />
          </div>
      
          <div ref={aboutRef} style={aboutOffset<windowHeight/2.5 ? {transition: 'opacity 1.5s', opacity: '1'} : {transition: 'opacity .8s', opacity: '0'}}>
            <About windowWidth={windowWidth}/>
          </div>

          <div ref={projectsRef} style={projectsOffset<windowHeight/2.5 ? {transition: 'opacity 1.5s', opacity: '1'} : {transition: 'opacity .8s', opacity: '0'}}>
            <Projects scrollPosition={scrollPosition} windowHeight={windowHeight} windowWidth={windowWidth} setOnScreenProject={setOnScreenProject} />
          </div>
          
        </main>

        <div ref={footerRef}>
          {windowWidth < 500 ?
            <>
              <MobileFooter />
            </>
            :
            <>
              {footerExpand ? <></> : <Footer/>}
            </>
          }  
        </div>
        
    </div>
  );
}

export default App;
