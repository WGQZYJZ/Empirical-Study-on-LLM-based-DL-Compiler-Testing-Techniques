
# Initializing the model
m1 = Attention()


Inputs to the model:
query_tensor  = torch.randn(64, 784)
key_tensor  = torch.randn(256, 784)
value_tensor  = torch.randn(256, 32, 10)


outputs from the model:
__output1__= m1(query_tensor, key_tensor, value_tensor)


# Description of requirements
The model should contain the following pattern:

