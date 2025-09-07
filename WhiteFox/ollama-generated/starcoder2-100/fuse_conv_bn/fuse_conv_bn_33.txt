

# Initializing the model
m = torch.nn.Conv3d(1, 128, kernel_size=5)
m = torch.nn.BatchNorm3d(128, eps=0.)

__output__  = m(input_tensor)

