
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
       v1 = self.conv(x1)
       v2 = torch.relu(v1)
       return v2

# Initializing the model
m_model = Model()

 # Inputs to the model
 x1 = torch.randn(3, 8, 64, 64)
 
 # Generating the first model output using forward method on the inputs and printing it as a string with 10 digits after decimal point 
 ouputModel  = m_model(x1).round(decimals=10)
 ouputModelString = f'{outputModel:10f}'
 print('ouputModelString')
 
 # Initializing the model and getting its string representation without round method and then printing it on the screen with 12 digits after decimal point. You can compare the output with the result from the first example of this task.
 m_model = Model()

 ouputModel = f'{m(x1):10f}'
 print('ouputModel')
 
 # Initializing the model and getting its string representation without round method using repr method on the inputs and printing it to screen with 12 digits after decimal point. You can compare the output with the result from the first example of this task. 
 m_model = Model()

 ouputModel = f'{m(x1):10f}'
 print('ouputModel')
 
 