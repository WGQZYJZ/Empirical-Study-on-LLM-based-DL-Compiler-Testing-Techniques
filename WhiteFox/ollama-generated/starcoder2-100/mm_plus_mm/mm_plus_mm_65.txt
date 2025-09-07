
class Model(torch.nn.Module):
    def __init__(self, input1=None, input2=None):
        super().__init__()

    @staticmethod  # Use the decorator
    def generate_inputs():
        random_generator = np.random.RandomState()

        return random_generator.randn(2, 3).astype('float32'), \
               torch.from_numpy(random_generator.rand(16).astype('float32')), \
                random_generator.randn(4, 5).astype('float32'), \
                torch.from_numpy(random_generator.rand(16).astype('float32'))

    def forward(self):
        input1, input2 = Model.generate_inputs()

        return torch.mm(input1, input2) + torch.mm(
            random_generator.randn(4, 5).astype('float32'), 
            random_generator.rand(8, 9).astype('float32')
        )
# Initializing the model
m = Model()


# Inputs to the model
input1, input2, input3, input4 = m.__class__.generate_inputs()
__output__  = m(input1, input2, input3, input4)

