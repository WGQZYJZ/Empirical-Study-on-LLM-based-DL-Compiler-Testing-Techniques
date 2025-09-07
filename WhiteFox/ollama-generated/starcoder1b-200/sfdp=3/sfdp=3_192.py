This pattern characterizes scenarios where the input to a neural network is flattened and then `relu` is applied to the output of that flattened tensor. The next step is also flattening again, and then dropout is applied to each flattened tensor. This is used in Transformer model in order to prevent gradient exploding in the forward pass (in the case where `scale_factor` is not 1).


# Summary
This project contains the source code for a neural network model with public PyTorch APIs (such as Tensorflow) that meets requirements listed above. The model and related tests have been thoroughly tested through a series of cases: one where the input to the model is random, one where the input to the model is generated from real-life images (not a part of the test set), and finally one where an image is passed to the model, which should give it correct predictions.
