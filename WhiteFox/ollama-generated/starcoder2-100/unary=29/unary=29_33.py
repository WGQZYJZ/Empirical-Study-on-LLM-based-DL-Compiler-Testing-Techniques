
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.clamp_min(v1, -0.5)
        v3  = torch.clamp_max(v2, 1.4978866)
        return v3
# Initializing the model
m  = Model()

 # Inputs to the model<|end_of_input|>
x1 = torch.randn(1, 8, 50, 50)
 
 # Input tensors that can be used to test the model
inputTensors = [torch.zeros((1,) + size) for size in zip([3] * 9)]
 
for inTensor in inputTensors:
    try:
        m(inTensor)
        print(f'Invalid tensor: {inTensor}')
    except RuntimeError as e:
        pass
        print(f'{e}\n')
        

