
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # Assume that the second argument is the input tensor A and permute it to 3D. Then, swap the 0-th and last dimension of this tensor. The 3D tensor will be used as an argument for the first argument of torch.bmm or torch.matmul.
        v1 = x2.permute(0, 2, 1)

        v2 = torch.nn.functional.linear(v1,  # Assume that the second argument is the input tensor B and permute it to 3D. Then, swap the 0-th and last dimension of this tensor. The 3D tensor will be used as an argument for the first argument of torch.bmm or torch.matmul
            x2.permute(0, 2, 1),
            x1
        )

        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(3)  # Assume that this is the input tensor B for the forward function of the model. The 0-th and last dimension should be swapped. 
x2  = torch.randn(1, 2, 2)

 __output__  = m(x1, x2)



# Model 2
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2): # Assume that the second argument is the input tensor A and permute it to 3D. Then, swap the 0-th and last dimension of this tensor. The 3D tensor will be used as an argument for the first argument of torch.bmm or torch.matmul.
        v1 = x2.permute(0, 2, 1)

        v2 = input_tensor_A.permute(0, 2, 1) # This is the input tensor A with its dimensions swapped. The first argument of this permute method is 3D.
        v3 = torch.nn.functional.linear(v2,  # Assume that the second argument is the input tensor B and permute it to 3D. Then, swap the 0-th and last dimension of this tensor. The 3D tensor will be used as an argument for the first argument of torch.bmm or torch.matmul
            x1.permute(0, 2, 1),
            input_tensor_B
        )

        return v3


# Initializing the model 2
m = Model()


 # Inputs to the model 2
x1 = torch.randn(2)  # Assume that this is the input tensor B for the forward function of the model. The 0-th and last dimension should be swapped. 
x2 = torch.randn(3, 4)

 __output__   = m(x1, x2)


