

# Initializing the model 
m = m.cuda() # Copying the model to GPU memory for better performance (If you don't want to do this, please ignore this line)

# Inputs to the model
x1 = torch.randn(32, 80, 64).cuda()

