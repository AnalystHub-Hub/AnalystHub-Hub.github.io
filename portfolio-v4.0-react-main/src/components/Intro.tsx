import { useEffect, useState } from 'react';
import Image from './cover';
import Typewriter from 'typewriter-effect';

type Props = {
    windowWidth: number;
}

export default function Intro({windowWidth}: Props) {
    const [introOpacity, setIntroOpacity] = useState(0);
    const [spanLeft, setSpanLeft] = useState(-1000);
    const [skew, setSkew] = useState('skewX(30deg)');
    
    const introStyle = {     
    //  paddingTop: 'calc(45vh - 40px)', 

    }
    const h1Style: object = {
        position: 'relative',
        transition: 'opacity 1.5s',
        transitionDelay: '.1s',
        opacity: introOpacity,
        lineHeight: 1,
        display: 'inline',
        whiteSpace: 'nowrap',
        zIndex: '1'
    }
    const spanStyle: object = {
        transition: 'left .4s cubic-bezier(.4,.43,0,1.23)',
        transitionDelay: '3.6s',
        position: 'relative',
        top: '-50px',
        left: windowWidth < 500 ? `${spanLeft-50}px` : `${spanLeft}px`,
        fontSize: windowWidth < 500 ? '6vw' : '70%',
    }
    const pStyle: object = {

        position: 'relative',
        top: '50px',
        left: windowWidth < 500 ? '0' :'60px',
        textAlign: windowWidth < 500 ? 'center' : 'left'
    }
    
    useEffect(() => {
        setIntroOpacity(1);
        setSpanLeft(50);
        setSkew('skewX(0deg)');
 
    }, []);

    return (
        <section id="intro" style={introStyle}>
            <h1 style={{transition: 'transform .1s', transitionDelay: '4s' , transform: skew, whiteSpace: 'nowrap'}}>
                <br/>
                <span style={spanStyle} className="accent">Data</span>
                <span style={{...spanStyle, transitionDelay: '3.8s'}} className="accent">&nbsp;Story&nbsp;Teller&nbsp;and&nbsp;Analyst.</span>
            
            </h1>

            <Image src="Tools.png"  isHidden={false} />
             <br/>
             <br/>
            <code style={pStyle}>
                <Typewriter
                    onInit={(typewriter) => {
                        typewriter
                        .pauseFor(5000) 
                        .typeString('scroll down and have a look.')    
                        .start();
                    }}
                    options={{
                        delay: 'natural'
                    }}
                />
            </code>
        </section>
    );
  }