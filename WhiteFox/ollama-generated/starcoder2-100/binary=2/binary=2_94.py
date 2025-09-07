
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)

# Initializing the model and getting the initial output of the model (to be used as a seed for input generation)

	# Seed
	s1  = torch.randn([3, 240])
	s2  = s1 - other
	x1  = torch.randn(1, 3, 64, 64).repeat_interleave(3, dim=0)  # To be used as a seed for input generation

	# Model initialization and initial output
	m  = Model()
	__output__  = m(x1)

