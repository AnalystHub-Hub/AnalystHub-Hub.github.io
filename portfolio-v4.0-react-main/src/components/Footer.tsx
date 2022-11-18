const stripeStyle = {
  
  borderStyle: 'solid',
  borderWidth: '0 0 1px 1px',
  borderColor: 'var(--accentcolor)',
  borderRadius: '0 6px 0px 6px',
  height: '10px',

}

export default function Footer() {
    return (
        <footer id="contact">
            <div id="h-stripe" style={stripeStyle}></div>
        </footer>
    );
  }