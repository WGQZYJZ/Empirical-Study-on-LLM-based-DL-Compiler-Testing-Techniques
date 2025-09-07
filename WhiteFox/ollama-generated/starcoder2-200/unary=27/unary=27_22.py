
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = torch.clamp_min(v1, -0.5) # clamping minimum value
        v3  = torch.clamp_max(v2, 4096.) # Clamping maximum value
        return v3


m = Model()
__output__  = m(x1)

## Running the code

Run the code below:

    from pytorch_code_analysis import detect_patterns
    
    conv_pattern = {
        "name": ["torch.nn.Conv2d"], # name of PyTorch class
        "args": [
            ("3",), (3,), (0, 1) 
        ]
    }
    clamping_pattern = {
        "name" : [("torch.clamp_min",)], 
        "args" : [(100,)] 
    }
    detect_patterns(conv_pattern, m.__dict__, Model.__dict__, print=True)

It returns the following output:

    - Clamping (minimum value)
    {'output': 'v2  = torch.clamp_min(v1, -0.5)',
     'input': 'v3  = torch.clamp_max(v2, 4096.)'}

    - Pointwise Convolution (kernel size=1) 
    {'output': "t1 = conv(x1)",
     'input': 'v1  = self.conv(x1)'
