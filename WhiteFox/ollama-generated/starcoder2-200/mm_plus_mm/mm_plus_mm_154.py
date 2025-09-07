
class Model(torch.nn.Module):
    def __init__(self, input1, input2, input3, input4):
        super().__init__()
        self.mm = torch.ops.rocm_smi.mm
        self.add  = torch.add
 
    def forward(self, x1, x2, x3, x4): 
        v0 = self.mm(x1, x2)
        v1 = self.mm(x3, x4)
        v2 = self.add(v0, v1) # Addition of the results of the two matrix multiplications
        return v2

# Initializing the model
m  = Model(input1=torch.randn((8, 6), device="cuda"),
            input2=torch.randn((450, 973), device="cuda"),
            input3=torch.randn((43, 43), device="cuda"), 
            input4=torch.randn((88, 3), device="cuda")
)

 # Inputs to the model
x1 = torch.randn(520, 973).to("cuda:0")
x2 = torch.randn(530, 530).to("cuda:0")
x3 = torch.randn(684, 3000).to("cuda:0")
x4 = torch.randn(179, 787).to("cuda:0")

 