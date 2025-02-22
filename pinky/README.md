# Pinky (Local)

### Tables
- Scan: Scan information of functional scans Baylor recorded. Total of 9 scans exist.
    - `scan_id`: Scan id ([2,3,4,5,6,9,10,11,12]).
    - `depth`: z index in the 2p structural stack (0 ~ 330).
    - `laser_power`: Laser power.
    - `wavelength`: Wavelength.
    
- Slice: Slice information of functional scans. 3 slices exist for each scan.
    - `scan_id`: Scan id of the slice.
    - `slice_idx`: Slice index within each scan ([1,2,3]).
    - `depth`: z index in the 2p structural stack (0 ~ 330).
    
- Stimulus: Visual stimulus used for the functional recording. The slices in each scan are recorded simultaneously.
    - `scan_id`: Scan id.
    - `movie`: Visual stimulus (90 x 160 x 27100 array). Time resolution is 14.83 frame/s. 
    - `condition`: Angle of the visual stimulus (length 27100 vector). Angles range between 0&deg; and 360&deg; with resolution of 22.5&deg;. The directions of the stimulus is pseudorandomly-ordered.
    
- Neuron: Cells in pinky100.
    - `segment_id`: Segment id in materialization `v185`.
    - `manual_id`: Id of manual masks drawn by Jake.
    
- Soma: Soma information.
    - `soma_x`: Soma x-axis location [nm]
    - `soma_y`: Soma y-axis location [nm]
    - `soma_z`: Soma z-axis location [nm]
    
- ManualMask: Manual masks.
    - `mask`: ROI mask (256 x 256 array). It matches the size of each functional video frame.

- ManualTrace: Trace from manual mask.
    - `trace_raw`: Raw traces.
    - `trace_detrend`: Detrended traces by high-pass filter.
    - `trace_dff`: Normalized traces (dF/F) where F is the mean of the first Gaussian fit when fitted with mixture of Gaussians of two.
    - `spike`: Deconvoluted traces using Vogelstein et al., 2009

- ManualTuning: Tuning curve computed from manual trace.
    - `orientation`: Orientation tuning curve (8 orientations). Value in each orientation is mean over trials.
    - `direction`: Direction tuning curve (16 directions). Valud in each direction is mean over trials.

- EASEMask: EASE masks.

- EASETrace: Trace from EASE mask.
    - `trace_raw`: Raw traces.
    - `trace`: Denoised and detrended traces.
    - `spike`: Deconvoluted traces using Vogelstein et al., 2009

- EASETuning: Tuning curve computed from EASE trace.
    - `orientation`: Orientation tuning curve (8 orientations). Value in each orientation is mean over trials.
    - `direction`: Direction tuning curve (16 directions). Valud in each direction is mean over trials.

- Segmentation: Segmentation version.
    - `segmentation`: Segmentation version.
    - `timestamp`: Time stamp that segmentation version was generated.
    
- Segment: Segments with 10 or more synapses in pinky100.
    - `segment_id`: Segment id in materialization `v185`.
    - `manual_id`: Id of manual masks.

- Mesh: Meshes of segments.
    - `n_vertices`: Number of vertices.
    - `n_triangles`: Number of triangles.
    - `vertices`: Mesh vertices [nm].
    - `triangles`: Triangle connectivity (python indexing).
