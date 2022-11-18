
import Nav from './Nav';

type Props = {
    hidden: boolean;
    scrollPosition: number;
    windowHeight: number;
    windowWidth: number;
}


export default function Header({hidden, scrollPosition, windowHeight, windowWidth}: Props) {

    const noBorder = (scrollPosition < 4);
    const style: any = {
        
        display: 'flex',
        flexDirection: (windowWidth < 500 ? 'column' : 'row'),
        top: '0px',
        borderStyle: 'solid',
        borderWidth: '0 0 1px 0',
        borderColor: 'var(--accentcolor)',
        boxShadow: '10px 10px 10px var(--shadowcolor)',
        backgroundColor: 'var(--bgcolortransparent)',
        zIndex: '100'
    }
    const titleStyle = {
        marginTop: "6px", 
        marginLeft: "6px", 
        fontSize: "1.5em",
    }
    if (hidden) {

        style.top = '-39px';
        
    }
    if (noBorder) {
        style.borderColor = '#00000000';
        style.boxShadow = 'none';
        style.backgroundColor = '#00000000';
    }


    return (
        <header style={style}>
            <div style={titleStyle}>
                {windowWidth < 500 ? <><span className="accent">N</span>MN</> : <><span className="accent">N.</span> Mondoa Nelson</> }
            </div>
            <Nav windowHeight={windowHeight} /> 
        </header>
    );
  }