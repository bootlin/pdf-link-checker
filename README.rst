================
pdf-link-checker
================
**pdf-link-checker** is a simple tool that parses a PDF document and checks for
broken hyperlinks. This done by sending a simple HTTP request to each link
found in a given document.

Getting it running
==================

::

    pip install pdf-link-checker
    pdf-link-checker my-awesome-slides.pdf

Options
=======

* --max-threads

  Specifies the maximum number of allowed threads (default: 100).

  To speedup the run, pdf-linkchecker will launch several threads
  in order to check several links in parallel.
  This option allows to set a limit to the number of threads.

* --max-requests-per-host

  Specifies the maximum number of allowed requests per host.

  Some URLs may belong to the same host, and since pdf-link-checker
  can check many URLs at the same time, we may want to set a limit
  to the number of requests per host.
  Otherwise, some hosts may confuse the check with a DoS attack.

Getting help
============

You can post your questions to our dedicated mailing list:

  http://lists.free-electrons.com/mailman/listinfo/pdf-link-checker-updates

TODO
====

*(...because there's no active project without a TODO list!)*

* Fix: Make it understand mailto links (such as mailto:foo@domain.com').

* Fix: some documents are failing on doc.initialize().

* Fix: ugly timeouts encountered when running the script.

* Replace the thread array into a nice thread pool.
  Each thread from the pool should take an URL from a (protected) queue.
  We could also have one queue per host and thus handle the
  max-requests-per-host constraint without a separate parameter.

Version History
===============

1.0.2
  * Updated repo location
  * Moved from distutils to setuptools

1.0.1
  * Version bump

1.0
  * Initial release
