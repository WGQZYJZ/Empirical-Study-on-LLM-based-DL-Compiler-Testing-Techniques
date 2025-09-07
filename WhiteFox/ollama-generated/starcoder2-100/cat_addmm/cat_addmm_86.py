
class Model(torch.nn.Module):
    def __init__(self, input_shape=[256], mat1_shape=[48930]):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(input_channels=1, 
                                                out_channels=7, 
                                                kernel_size=(3)) 
        self.linear1 = nn.Linear(in_features=mat1_shape[0], out_features=48930)
        self.linear2 = nn.Linear(48930, mat1_shape[0])

        mat1  = torch.randn(*mat1_shape).to("cuda")
        mat2  = torch.randn(*mat1_shape).to("cuda")

    def forward(self, x): 
        v1 = self.conv(x)
        v2 = self.linear1(v1)
        v3 = self.linear2(v2)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model  
input_data = torch.rand(*input_shape).to("cuda")  
 __output__  = m(input_data)
 
