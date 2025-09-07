
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5)
        self.conv2 = torch.nn.ConvTranspose2d(4096, 32, 7)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x):
        v1 = conv1(x)
        v2 = conv2(v1)
        v3 = sigmoid(v2)
        return v3


# Initializing the model and setting seed 42 for reproducibility.
m = Model().cuda()
seed_torch(42)
 
# Generating inputs to the model
x = torch.randn(8, 3, 128, 128).cuda()
 
# Running the model on the inputs and printing the output shape
with torch.no_grad():
    outputs = m(x)
print('output shape: ', outputs.shape)

