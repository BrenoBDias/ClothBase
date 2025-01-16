function PP (){

    const imageUrl = './src/assets/profilepic.png'

    const HandleClick = (e) => e.target.style.display = "none"

    return(
       <img onClick={(e) => HandleClick(e)} src={imageUrl} alt="Profile Pic" /> 
    )

}

export default PP