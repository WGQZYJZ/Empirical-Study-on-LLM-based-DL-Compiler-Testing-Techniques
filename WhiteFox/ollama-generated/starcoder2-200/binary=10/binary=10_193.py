
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self._layer = torch.nn.Linear(2, 3)
 
    def forward(self, x1):

        # Applying a linear transformation to the input tensor and adding another tensor.
        v_t = self._layer(x1)
        out = v_t + other
 
        return out
 
# Initializing the model with randomly initialized weights/biases
m  = Model()

 # Generating two random tensors as the input of the model
x1, x2  = torch.randn(3, 4), torch.randn(3)
