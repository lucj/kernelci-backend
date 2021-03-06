.. _schema_compare:

compare
-------

.. _schema_compare_get:

GET
***

.. _schema_compare_get_job:

job
###

The following schema covers the data available in the result of a ``job-compare`` operation.

.. literalinclude:: schema/1.0/get_compare_job.json
    :language: json

**Notes**

* The items in the array that contains the status results, in the ``delta_result`` array, can be: strings that identify the build status or null. In case of a null value, it means that the build in that position was not available.

.. _schema_compare_post:

POST
****

.. _schema_compare_post_job:

job
###

The following schema covers the data that should be available in the JSON data
to perform a POST request on the ``job-compare`` resource (:ref:`more info <collection_job>`).

.. literalinclude:: schema/1.0/post_compare_job.json
    :language: json

**Notes**

* It is necessary to include either the ``job_id`` value or both ``job`` and ``kernel``. If all are specified, ``job_id`` will be used.


