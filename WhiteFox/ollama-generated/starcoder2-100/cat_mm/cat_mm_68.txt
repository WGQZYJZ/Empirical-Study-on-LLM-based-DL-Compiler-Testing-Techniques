
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.conv2d  = torch.nn.Conv2d(4096+3, 512, kernel_size=(7, 7), stride=2, padding=3)
 
    def forward(self):
        t1  = F.pad(input1.unsqueeze(-1).permute([0, 1]), (3, 3))
        t2 = torch.matmul(t1, input2)
	t4 = self.conv(t2)
	t5 = self.conv2d(t4)
        return t6

 # Initializing the model with randomly generated inputs