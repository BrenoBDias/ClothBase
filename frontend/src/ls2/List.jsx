function List(props) {

    const fruits = [{id: 1, name: "apple", cal: 95},
                    {id: 2, name: "orange", cal: 45},
                    {id: 3, name: "banana", cal: 105},
                    {id: 4, name: "coconut", cal: 159},
                    {id: 5, name: "pineapple", cal: 37}];
    

    const listItens = fruits.map(fruit => <li key={fruit.id}>{fruit.name}</li>);

    return(<ol>{listItens}</ol>
    );

}

export default List