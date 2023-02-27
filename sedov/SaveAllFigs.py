# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1449, 919]

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10.92820323027551]
renderView1.CameraFocalPoint = [0.0, 0.0, -1e-20]
renderView1.CameraParallelScale = 2.384293939868689

# save screenshot
SaveScreenshot('/home/andresrueda/remote/rocinante_scratch/20221123_MCL_LGL/paper_MCL_LGL/examples/figures/sedov/densforall_seq_rho.png', renderView1, ImageResolution=[1449, 919])

# get active source.
solution_vtu = GetActiveSource()

# get display properties
solution_vtuDisplay = GetDisplayProperties(solution_vtu, view=renderView1)

# set scalar coloring
ColorBy(solution_vtuDisplay, ('POINTS', 'shock_capturing_alpha_rho'))

# get color transfer function/color map for 'rho'
rhoLUT = GetColorTransferFunction('rho')

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(rhoLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
solution_vtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
solution_vtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'shock_capturing_alpha_rho'
shock_capturing_alpha_rhoLUT = GetColorTransferFunction('shock_capturing_alpha_rho')

# get opacity transfer function/opacity map for 'shock_capturing_alpha_rho'
shock_capturing_alpha_rhoPWF = GetOpacityTransferFunction('shock_capturing_alpha_rho')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10.92820323027551]
renderView1.CameraFocalPoint = [0.0, 0.0, -1e-20]
renderView1.CameraParallelScale = 2.384293939868689

# save screenshot
SaveScreenshot('/home/andresrueda/remote/rocinante_scratch/20221123_MCL_LGL/paper_MCL_LGL/examples/figures/sedov/densforall_seq_alpha_rho.png', renderView1, ImageResolution=[1449, 919])

# set scalar coloring
ColorBy(solution_vtuDisplay, ('POINTS', 'shock_capturing_alpha_rho_v1'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(shock_capturing_alpha_rhoLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
solution_vtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
solution_vtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'shock_capturing_alpha_rho_v1'
shock_capturing_alpha_rho_v1LUT = GetColorTransferFunction('shock_capturing_alpha_rho_v1')

# get opacity transfer function/opacity map for 'shock_capturing_alpha_rho_v1'
shock_capturing_alpha_rho_v1PWF = GetOpacityTransferFunction('shock_capturing_alpha_rho_v1')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10.92820323027551]
renderView1.CameraFocalPoint = [0.0, 0.0, -1e-20]
renderView1.CameraParallelScale = 2.384293939868689

# save screenshot
SaveScreenshot('/home/andresrueda/remote/rocinante_scratch/20221123_MCL_LGL/paper_MCL_LGL/examples/figures/sedov/densforall_seq_alpha_rho_v1.png', renderView1, ImageResolution=[1449, 919])

# set scalar coloring
ColorBy(solution_vtuDisplay, ('POINTS', 'shock_capturing_alpha_rho_v2'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(shock_capturing_alpha_rho_v1LUT, renderView1)

# rescale color and/or opacity maps used to include current data range
solution_vtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
solution_vtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'shock_capturing_alpha_rho_v2'
shock_capturing_alpha_rho_v2LUT = GetColorTransferFunction('shock_capturing_alpha_rho_v2')

# get opacity transfer function/opacity map for 'shock_capturing_alpha_rho_v2'
shock_capturing_alpha_rho_v2PWF = GetOpacityTransferFunction('shock_capturing_alpha_rho_v2')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10.92820323027551]
renderView1.CameraFocalPoint = [0.0, 0.0, -1e-20]
renderView1.CameraParallelScale = 2.384293939868689

# save screenshot
SaveScreenshot('/home/andresrueda/remote/rocinante_scratch/20221123_MCL_LGL/paper_MCL_LGL/examples/figures/sedov/densforall_seq_alpha_rho_v2.png', renderView1, ImageResolution=[1449, 919])

# set scalar coloring
ColorBy(solution_vtuDisplay, ('POINTS', 'shock_capturing_alpha_rho_e'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(shock_capturing_alpha_rho_v2LUT, renderView1)

# rescale color and/or opacity maps used to include current data range
solution_vtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
solution_vtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'shock_capturing_alpha_rho_e'
shock_capturing_alpha_rho_eLUT = GetColorTransferFunction('shock_capturing_alpha_rho_e')

# get opacity transfer function/opacity map for 'shock_capturing_alpha_rho_e'
shock_capturing_alpha_rho_ePWF = GetOpacityTransferFunction('shock_capturing_alpha_rho_e')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10.92820323027551]
renderView1.CameraFocalPoint = [0.0, 0.0, -1e-20]
renderView1.CameraParallelScale = 2.384293939868689

# save screenshot
SaveScreenshot('/home/andresrueda/remote/rocinante_scratch/20221123_MCL_LGL/paper_MCL_LGL/examples/figures/sedov/densforall_seq_alpha_rho_e.png', renderView1, ImageResolution=[1449, 919])

# set scalar coloring
ColorBy(solution_vtuDisplay, ('POINTS', 'shock_capturing_alpha_pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(shock_capturing_alpha_rho_eLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
solution_vtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
solution_vtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'shock_capturing_alpha_pressure'
shock_capturing_alpha_pressureLUT = GetColorTransferFunction('shock_capturing_alpha_pressure')

# get opacity transfer function/opacity map for 'shock_capturing_alpha_pressure'
shock_capturing_alpha_pressurePWF = GetOpacityTransferFunction('shock_capturing_alpha_pressure')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10.92820323027551]
renderView1.CameraFocalPoint = [0.0, 0.0, -1e-20]
renderView1.CameraParallelScale = 2.384293939868689

# save screenshot
SaveScreenshot('/home/andresrueda/remote/rocinante_scratch/20221123_MCL_LGL/paper_MCL_LGL/examples/figures/sedov/densforall_seq_alpha_pressure.png', renderView1, ImageResolution=[1449, 919])

# set scalar coloring
ColorBy(solution_vtuDisplay, ('POINTS', 'shock_capturing_alpha_entropy'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(shock_capturing_alpha_pressureLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
solution_vtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
solution_vtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'shock_capturing_alpha_entropy'
shock_capturing_alpha_entropyLUT = GetColorTransferFunction('shock_capturing_alpha_entropy')

# get opacity transfer function/opacity map for 'shock_capturing_alpha_entropy'
shock_capturing_alpha_entropyPWF = GetOpacityTransferFunction('shock_capturing_alpha_entropy')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10.92820323027551]
renderView1.CameraFocalPoint = [0.0, 0.0, -1e-20]
renderView1.CameraParallelScale = 2.384293939868689

# save screenshot
SaveScreenshot('/home/andresrueda/remote/rocinante_scratch/20221123_MCL_LGL/paper_MCL_LGL/examples/figures/sedov/densforall_seq_alpha_entropy.png', renderView1, ImageResolution=[1449, 919])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10.92820323027551]
renderView1.CameraFocalPoint = [0.0, 0.0, -1e-20]
renderView1.CameraParallelScale = 2.384293939868689

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
