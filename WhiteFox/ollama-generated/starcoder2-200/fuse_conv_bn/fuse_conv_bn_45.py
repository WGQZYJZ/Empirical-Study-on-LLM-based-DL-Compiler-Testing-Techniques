

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.conv2d(x1, kernel)

        bn  =  self.batchnorm(v2)
        return bn

class BN(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, conv_output):
        v3  = torch.nn.functional.batch_norm(conv_output)
        return v3

 # Initializing the model
 m1 = Model()
 m2 = Model()
 
 # Inputs to the models
 x1  = torch.randn(1, 32, 10, 98) 
 x2  = torch.randn(1, 64, 5, 7)

 __output__m1_0 = m1(x1)  
 __output__m1_1 = m1(x2)
 __output__m2_0 = m2(x1) 
 __output__m2_1 = m2(x2)

 