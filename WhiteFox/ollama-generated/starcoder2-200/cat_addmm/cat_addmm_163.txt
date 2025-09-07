
class Model(torch.nn.Module):
    def __init__(self, inputSize, outputSize):
        super().__init__()
        self.inputSize = 14
        self.outputSize = 64
        self.linear1  = torch.nn.Linear(self.inputSize, self.outputSize)
        self.linear2  = torch.nn.Linear(self.outputSize, outputSize)
 
    def forward(self, x):
        v0  = x 
        v1  = self.linear1(v0) # Fully connected layer followed by an activation function
        v3  = torch.tanh(v1) * math.sqrt(2/self.inputSize) # Apply the Tanh activation function to a fully connected layer, then scale its output to have zero mean and unit variance
        v4  = self.linear2(v0) # Fully connected layer followed by an activation function
        v5  = torch.sigmoid(v3 + v4) # Apply sigmoid (inverse of the Tanh activation function)
        return v5 


# Initializing the model with the initial tensor and size of the input/output tensors:

<jupyter_code>def forward_layer_01(inputSize, outputSize):
    m = Model(inputSize, outputSize).cuda()
    x = torch.randn(234978, 14)
    y = torch.zeros([657]).long().cuda() # Initializing an output tensor
    return m(x), y
<jupyter_output><empty_output><jupyter_text># Initializing the model with the initial tensor and size of the input/output tensors:

<jupyter_code>def forward_layer_02(inputSize, outputSize):
    m = Model(inputSize, outputSize).cuda()
    x  = torch.randn([347], [14])
    y = torch.zeros([658]).long().cuda() # Initializing an output tensor 
    return m(x), y
<jupyter_output><empty_output>