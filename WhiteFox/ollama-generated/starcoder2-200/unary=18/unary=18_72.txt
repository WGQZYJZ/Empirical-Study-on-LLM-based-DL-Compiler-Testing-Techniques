

model = torch.nn.Sequential(torch.nn.Conv2d(3,8,kernel_size=1),torch.nn.ReLU())
model = torch.jit.script(model)
model

