
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other 
        v3  = torch.relu(v2) # Apply ReLU to output of the convolution
        return v3

# Initializing model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)


# Other inputs or tensors that are not used during training, but need to be passed to the model during testing for the evaluation of accuracy/precision/recall etc., need to be passed as inputs to the model as follows:
other = torch.randn(1,320,10,5) # The size is chosen randomly to demonstrate the user should find a tensor or other input that works for this model example. You may want to use a larger random integer instead of 1 if your model is more complex and there are many such parameters that you want to feed during evaluation/testing of your model.


