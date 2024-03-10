# ClothBase

ClothBase is a database designed for artisans to efficiently categorize and store pictures of their materials. This tool aims to streamline the process of material selection by providing artisans with a visual inventory of their resources. With ClothBase, artisans can easily browse through their collection, make informed decisions on material usage, and locate specific materials when needed.

## Features:

- **Material Categorization**: Organize materials into custom categories for easy navigation.
- **Visual Inventory**: Store pictures of materials to provide a visual reference.
- **Search Functionality**: Quickly find specific materials using search filters.
- **Material Details**: Include additional information such as material type, source, and quantity.

## Why ClothBase?

Traditional methods of material management can be time-consuming and inefficient. ClothBase offers a modern solution to streamline the process, saving artisans valuable time and resources. By centralizing material information in one accessible platform, ClothBase empowers artisans to make informed decisions and optimize their creative workflow.
---
## Reference Images:

![alt text](https://github.com/BrenoBDias/ClothBase/blob/main/Images/6L0UM5XVMlAAAAAElFTkSuQmCC.png)

![alt text](https://github.com/BrenoBDias/ClothBase/blob/main/Images/wULxAyFHVUVPgAAAABJRU5ErkJggg.png)

![alt text](https://github.com/BrenoBDias/ClothBase/blob/main/Images/w8Dk6LMtTp2sQAAAABJRU5ErkJggg.png)

---

## Requirements:
The program is designed to run on any personal computer with at least 4 cores of processing.

## Major components:
The major components of the program are the GUI and the backend, which will both be constrained to the same application by enabling multithreading, and the Database, which will save, manage and maintain the information about the program's files.

## Technology:
The program is simple. It is written and designed in python as its language, with a GUI based on pyqt. The Database uses mySQL.

## Data Model:
   - ### Materials Table:
     - Attributes:
       - ID: Unique identifier for the material.
       - Name: Name of the material.
       - Image: File path or reference to the locally stored image of the material.
       - Category ID: Identifier linking the material to its category.
       - Source: Source or supplier of the material.
       - Quantity: Quantity of the material available.
       - Price per unity: Price payed per unity of the material when it was acquired.
       - Added Timestamp: Timestamp indicating when the material was added to the database.
   - ### Categories Table:
     - Attributes:
       - ID: Unique identifier for the category.
       - Name: Name of the category.