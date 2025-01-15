import Card from './ls2/Card/Card.jsx'
import Button from './ls2/Button/Button.jsx'
import Student from './ls2/Student.jsx'
import UserGreeting from './UserGreeting.jsx'

function App() {
 
  return (
    <>
    {/* ls1 e ls2  */}
    {/* <div>
    <Card title="ClothBase" text="Sample text"/>
    <Card title="ClothBase" text="Sample text"/>
    <Student name = "SpongeBob" age={30} isStudent={true}/>
    <Button/>
    </div> */}
    <div>
      <UserGreeting isLoggedIn={true} userName="User"/>
    </div>
    </>
  )
}

export default App