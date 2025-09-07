

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(25088,1)
    
    def forward(self, x1):
        
        v1  = self.linear(x1)
        v2  = v1 * 0.7364978773617745
        v3  = torch.erf(v2)
        v4  = v3 + 0.8841991129777884
        v5  = v2 * v4
        
        return v5

# Initializing the model and set the optimizer/loss function for backpropagation.
m  = Model()
optimizer_state_dict  = {
	'states': {
		0: {
				'params': [
					{
						'mask': (1L, False),
						'target': (3L,)
					}
				],
				'dict': {
					'2865749.528793378_f214b160-a9bd-11ea-9d5b-3c3a3e03c1d1': {
						'mask': 'f214b160-a9bd-11ea-9d5b-3c3a3e03c1d1',
						
					},
					'2865749.528793378_19f82b90-a9be-11ea-9d5b-3c3a3e03c1d1': {
						'mask': '19f82b90-a9be-11ea-9d5b-3c3a3e03c1d1',
						
					},
					'2865749.528793378_b0325cb0-a9bc-11ea-9d5b-3c3a3e03c1d1': {
						'mask': 'b0325cb0-a9bc-11ea-9d5b-3c3a3e03c1d1',
						
					},
					'2865749.528793378_555252aa-a9bd-11ea-9d5b-3c3a3e03c1d1': {
						'mask': '555252aa-a9bd-11ea-9d5b-3c3a3e03c1d1',
						
					},
					'2865749.528793378_8188568e-a9bb-11ea-9d5b-3c3a3e03c1d1': {
						'mask': '8188568e-a9bb-11ea-9d5b-3c3a3e03c1d1',
						
					}
				},
				
			},
		47: {
				'dict': {
					'313f93f2-a9bd-11ea-9d5b-3c3a3e03c1d1_d947a8ac-a9bb-11ea-9d5b-3c3a3e03c1d1': {
						'mask': '313f93f2-a9bd-11ea-9d5b-3c3a3e03c1d1',
						
					},
				}
			}
		},
	'optim': {
		
	}
}
#m = Model()
optimizer  = torch.optim.Adam(params=m.parameters(), lr=.2)

