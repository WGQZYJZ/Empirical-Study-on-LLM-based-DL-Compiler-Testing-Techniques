This pattern characterizes scenarios where the tensors are modified before feeding them into the forward function, and it is done in either training or inference mode. In the former case, the model will be trained, and in the latter case, we will perform inference.


# Code of generation
`generate_input.py`: This script generates the input to the generated model and generates the input to the forward function, `forward`. The user should run this script once before generating the input, and it does not change the models or inputs in any way.

`generate_model.py`: This script takes the model example and generates the PyTorch model class. The model is also saved in a binary file.

