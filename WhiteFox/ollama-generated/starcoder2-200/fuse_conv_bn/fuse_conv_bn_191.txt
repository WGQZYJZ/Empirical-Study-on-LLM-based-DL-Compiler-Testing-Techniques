
# Initializing the model
m  = torch.nn.Conv2d(3, 64, kernel_size=7)
n = torch.nn.BatchNorm2d(32) # n.running_mean and n.running_var are used as input


# Inputs to the model
input_tensor1 = torch.randn(10, 3, 5, 4).cuda() 
input_tensor2 = torch.randn(30, 64, 7).cuda() 

# Executing model with F.conv2d, not directly with nn.Conv2d (to test fusion)
output1  = n(F.conv2d(input_tensor1, m.weight)) # m is in train mode because of the BN layer 
output2  = n(nn.functional.conv2d(input_tensor1, m.weight))

