abstract_text = """Remote sensing image scene classification plays an
important role in a wide range of applications and hence has been
receiving remarkable attention. During the past years, significant
efforts have been made to develop various datasets or present a
variety of approaches for scene classification from remote sensing
images. However, a systematic review of the literature concerning
datasets and methods for scene classification is still lacking. In
addition, almost all existing datasets have a number of limitations,
including the small scale of scene classes and the image numbers,
the lack of image variations and diversity, and the saturation of
accuracy. These limitations severely limit the development of new
approaches especially deep learning-based methods. This paper
first provides a comprehensive review of the recent progress. Then,
we propose a large-scale dataset, termed "NWPU-RESISC45",
which is a publicly available benchmark for REmote Sensing
Image Scene Classification (RESISC), created by Northwestern
Polytechnical University (NWPU). This dataset contains 31,500
images, covering 45 scene classes with 700 images in each class.
The proposed NWPU-RESISC45 (i) is large-scale on the scene
classes and the total image number, (ii) holds big variations in
translation, spatial resolution, viewpoint, object pose, illumination,
background, and occlusion, and (iii) has high within-class diversity
and between-class similarity. The creation of this dataset will
enable the community to develop and evaluate various data-driven
algorithms. Finally, several representative methods are evaluated
using the proposed dataset and the results are reported as a useful
baseline for future research."""

overview_text = """The currently available instruments (e.g., multi/hyperspectral
[1], synthetic aperture radar [2], etc.) for earth observation [3, 4]
generate more and more different types of airborne or satellite
images with different resolutions (spatial resolution, spectral
resolution, and temporal resolution). This raises an important
demand for intelligent earth observation through remote sensing 
images, which allows the smart identification and classification
of land use and land cover (LULC) scenes from airborne or
space platforms [3]. Remote sensing image scene classification,
being an active research topic in the field of aerial and satellite
image analysis, is to categorize scene images into a discrete set
of meaningful LULC classes according to the image contents.
During the past decades, remarkable efforts have been made in
developing various methods for the task of remote sensing
image scene classification because of its important role for a
wide range of applications, such as natural hazards detection
[5-7], LULC determination [8-43], geospatial object detection
[27, 44-52], geographic image retrieval [53-63], vegetation
mapping [64-68], environment monitoring, and urban planning. 
In the early 1970s, the spatial resolution of satellite images
(such as Landsat series) is low and hence, the pixel sizes are
typically coarser than, or at the best, similar in size to the objects
of interest [69]. Most of the methods for image analysis using
remote sensing images developed since the early 1970s are
based on per-pixel analysis, or even sub-pixel analysis for this 
 
conversion [69-72]. With the advances of remote sensing
technology, the spatial resolution is gradually finer than the
typical object of interest and the objects are generally composed
of many pixels, which has significantly increased the within
class variability and single pixels do not come isolated but are
knitted into an image full of spatial patterns. In this case, it is
difficult or sometimes impoverished to categorize scene images
at pixel level purely."""

methods_text = """During the last decades, considerable efforts have been made 
to develop various methods for the task of scene classification
using satellite or aerial images. As scene classification is usually
carried out in feature space, effective feature representation
plays an important role in constructing high-performance scene
classification methods. We can generally divide existing scene
classification methods into three main categories according to
the features they used: handcrafted feature based methods,
unsupervised feature learning based methods, and deep feature
learning based methods. It should be noted that these three
categories are not necessarily independent and sometimes the
same method exists with different categories."""

results_text = """To make a comprehensive evaluation, two training-test ratios
are considered. (i) 10%-90%: the dataset was randomly split
into 10% for training and 90% for testing (70 training samples
and 630 testing samples per class). (ii) 20%-80%: the dataset
was randomly divided into 20% for training and 80% for testing
(140 training samples and 560 testing samples per class).

For BoVW, BoVW+SPM and LLC methods, we adopted the
widely used densely sampled SIFT descriptor to describe each
image patch with the patch size set to be 16×16 pixels and the
grid spacing to be 8 pixels to balance the speed/accuracy
trade-off, which is the same as the research work of [86]. The
sizes of visual codebooks were set to be 500, 1000, 2000, and
5000, respectively, to study how they affected the classification performance.

The AlexNet model, VGGNet-16 model, and GoogLeNet
model, which were pre-trained on ImageNet dataset [175], are
obtained from https://github.com/BVLC/caffe/wiki/Model-Zoo
for deep CNN feature extraction. To further improve their
generalization capability, we also fine-tuned them by using the
parameters as summarized in Table 2. All three CNN models
were implemented on a PC with 2 2.8GHz 6-core CPUs and
32GB memory. Besides, a GTX Titan X GPU was also used for
acceleration."""

further_text = """The significant development of remote sensing technology
over the past decade has been providing us explosive remote
sensing data for intelligent earth observation such as scene
classification using remote sensing images. However, the lack
of publicly available "big data" of remote sensing images
severely limits the development of new approaches especially
deep learning based methods. This paper first presented a
comprehensive review of the recent progress in the field of
remote sensing image scene classification, including benchmark
datasets and state-of-the-art methods. Then, by analyzing the
limitations of the existing datasets, we proposed a large-scale,
freely and publicly available benchmark dataset to enable the
community to develop and evaluate new data-driven algorithms.
Finally, we evaluated a number of representative state-of-the-art
methods including deep learning based methods for the task of
scene classification using the proposed dataset and reported the
results as a useful performance baseline for future research.

However, until now, almost all scene classification methods
rely on only traditional remote sensing, i.e., overhead imagery,
to distinguish different types of land-cover in a given region. In
fact, the more recent development of social media and spatial
technology has significant potential for complimenting the
shortcoming of traditional means of scene classification. First,
the rapid development of social media especially the on-line
photo sharing websites, such as Flickr, Panoramio, and
Instagram, have been collecting sorts of information of ground
objects from geo-tagged ground photo collections. Second, by
linking earth observation data coming from satellites and
geographic information systems (GIS) to location-aware spatial
technologies, such as global positioning system (GPS), wireless
fidelity (WIFI), and smart-phones, we are locating at a powerful
geographic information system in which we can readily know, at
any time, where every ground object is located on the surface of
the Earth. Therefore, we can say that these geo-tagged ground
photo collections and location-based geographic resources act
as a repository of all kinds of information, including who, what,
where, when, why, and how. This allows us to perform
knowledge discovery by crowdsourcing of information through
these location-based social medial data. For example, using
only remote sensing images, it is more difficult to tell where a
certain object comes from, but with Twitter generating more
than 500 million Tweets per day (of which a good portion are
tagged with latitude-longitude coordinates), we can map
"what-is-where" easily on the surface of the Earth using the
"what" and "where" aspects of the information. Besides,
compared with remote sensing images, the ground photos
uploaded by user holds higher resolution and are quite different
from satellite remote sensing in the observation direction, which
can well capture the detail and vertical characteristics of ground
objects. All the additional information is in fact very useful for
the classification and recognition of remote sensing images
because it could better help individuals learn more powerful (or
multi-view) feature representations. Consequently, in the future
work we need to explore new methods and systems in which the
combination of remote sensing data and information coming
from social media and spatial technology can be deployed to
promote the state-of-the-art of remote sensing image scene
classification."""
