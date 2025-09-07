
class Model(torch.nn.Module):
    def __init__(self, size=320):
        super().__init__()
        self.size = size
 
    def forward(self, x1, y1):
        t1 = torch.cat([x1, y1], dim=1)  # Concatenate input tensors along dimension 1
        t2 = t1[:, :9223372036854775807]  # Slice the concatenated tensor along dimension 1
        t3 = t2[:self.size, :]  # Further slice the tensor along dimension 1
        t4 = torch.cat([t1, t3], dim=1)  # Concatenate the original concatenated tensor and the sliced tensor along dimension 1 
        return t4

# Initializing the model with size 80
m = Model(size=80)
 
# Inputs to the model
x1 = torch.randn(32, 150, 64, 70) # Input tensors for x_1 dimension (N, Cin * kernel_h * kernel_w) of shape [32, 90, 80] where N is the number of examples in a mini-batch.
y1 = torch.randn(32, 50, 64, 70) # Input tensors for y_1 dimension (N, Cin * kernel_h * kernel_w) of shape [32, 90] where N is the number of examples in a mini-batch.
 
