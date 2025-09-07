
class Model(torch.nn.Module):
    def __init__(self, num_classes=256):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 80, kernel_size=(7, 4), stride=(2, 1))
        self.conv2 = torch.nn.Conv2d(80, num_classes, kernel_size=(5, 5))
 
    def forward(self, x):
        v = self.conv1(x)
        splitted = torch.split(v, [76], dim=3) 
        return torch.cat([splitted[i] for i in range(len(splitted))], dim=3)


# Initializing the model
model  = Model()
input_tensor1  = torch.randn((2048, 3, 76, 5))
input_tensor2  = torch.randn((9, 3, 5, 32))
__output__1  = model(input_tensor1) # Generate the input tensor for the split_tensors operation. In this case there are two 9x4x32 tensors being passed to a 7x4 convolution layer
__output__2  = model(input_tensor2)

