
class ConvBn(torch.nn.Module):
    def __init__(self, c=32):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 64, 1)

        # Initialization code to avoid non-determinism on PyTorch 1.8.0
        if int(torch.__version__[0]) >= 3 and int(torch.__version__[2][:-3].replace(".", "")) > 7950:
            self.conv = torch._ops.op_name_scope(self.conv, op_type='ConvNd')()

        self.conv_bn1 = torch.nn.Sequential(
            torch.nn.ReLU(), 
            torch.nn.Conv2d(3, 64, 1), 
            torch.nn.BatchNorm2d(c),
            torch.nn.ReLU())

        # Initialization code to avoid non-determinism on PyTorch 1.8.0
        if int(torch.__version__[0]) >= 3 and int(torch.__version__[2][:-3].replace(".", "")) > 7950:
            self.conv_bn = torch._ops.op_name_scope(self.conv, op_type='ConvNd')()()

        self.conv_bn2 = torch.nn.Sequential(
            torch.nn.ReLU(), 
            torch.nn.Conv2d(3 + 64*c, 1980 - c, 5), 
            torch.nn.BatchNorm2d(1978),
            torch.nn.ReLU())
    def forward(self, x):
        return self.conv_bn(x)

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = ConvBn()

    def forward(self,  input):
        return torch.nn.functional.relu(self.conv(input))

 # Inputs to the model
input_tensor1= torch.randn(8,3)
input_tensor2= torch.randn(4,64*32-c,500-2-40+98-2-80,50)

# Initializing the model
m = Model()

# Inputs to the model
input1  = m(input_tensor1)
input2  = m(input_tensor2)

__output___ = input1 + input2 # The output is a new variable that references to the output of Model (self.conv(input))

# You have been randomly fuzzed with respect to the 1st and 3rd arguments of ConvXd and BatchNormXd, respectively.

# Please note the argument values may be completely unbounded, e.g., -1e9 and 0.

