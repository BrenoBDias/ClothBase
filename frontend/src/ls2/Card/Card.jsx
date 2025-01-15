import styles from './Card.module.css'
function Card(props) {
   
    
    return(
        <div className = {styles.card}>
            <img className={styles.cardImage} src="https://placehold.co/150x150/gray/black" alt="Clothbase Logo"></img>
            <h2 className={styles.cardTitle}>{props.title}</h2>
            <p className={styles.cardText}>{props.text}</p>

        </div>
    )
}

export default Card