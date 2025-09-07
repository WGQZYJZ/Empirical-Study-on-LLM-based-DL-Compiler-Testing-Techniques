
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)

        # Substracting a scalar from the output of a pointwise convolution
        v2_tensor = torch.randn([1])
        v2 = v1 - 0.5

        # Substracting another model's output tensor (from its forward function) from the result of the first pointwise convolution subtraction operation
        v3 = v2_tensor  # <-- Replace this line with a Tensor that contains a PyTorch model's forward outputs. You may need to call the model's forward method, and save its output in a Tensor named "v1".
        v4 = v3 - v1

        # Using ReLU activation function as an example of custom function
        v5 = torch.nn.functional.relu(v2) 

        return v4

# Initializing the model
m = Model()

