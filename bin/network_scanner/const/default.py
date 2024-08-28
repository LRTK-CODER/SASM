# -*- coding: utf-8 -*-
# 
# Script : network_scanner/const/default.py
# Author : Hoon
# 
# ====================== Comments ======================
# 

# Python Libraries
import os
from textwrap import dedent
from ctypes   import windll
from sys      import platform as sys_platform

ASCII_ART = dedent( """
                                                *
                                               **             *   *        
                                               *                 *         
                                         * *   *              *            
                                           **  **              **          
                                               **              *        *  
                                                 **           *    *  **   
                                                   ***      ***   * ***    
                                                       ************        
                                                             ****          
                                                         **********        
                                                          ***********      
                                                           ******* *****   
                                                           ****************
                                                          ***** ***********
                                                         *****  *****      
        ****                          ****             ******  ****        
     *********         ***          ********     ****  ****** *****        
     **               *****        **            ***** ***** *****         
     ***             ***  **       ***           ****** ***  *****         
      *******        **   ***       *******      **  **  *  **  **         
           ****     **     **            ****    ***  **   **   **         
             **    ***********             ***   ****  ** ***   **         
     **     ***   ***       ***    **      **    ***** *****    **         
     ********     **         ***    ********  *  *****  ***     **         
                                            ***  ******                    
            **                        *******************                  
             *******************************************                   
              *************************    **************                  
             ***************                ****   ********                
         ***********  ******                ****       ******              
        *********     *****                 ***           ***              
        ****         *****                  ***           ***              
       ***           *****                  ***          **                
      ***             ****                  **          **                 
     ***                ***                 **         **                  
     **                   **                *        ***                   
    **                     ***             **      ***                     
   ***                       **            **                              
  ***                         **           **                              
 **                             **         **                              
                                 *          **
""" )

MODULE  = 'SASM - Network Scanner'
VERSION = '1.0.0'

#######################################################################################
# Platform
#######################################################################################
if sys_platform == 'win32':
    WIN32       = True
    ESCAPE_CHAR = '^'
    ENV_SEP     = ';'
    DIR_SEP     = '\\'

else:
    WIN32       = False
    ESCAPE_CHAR = '\\'
    ENV_SEP     = ':'
    DIR_SEP     = '/'

#######################################################################################
# System
#######################################################################################
try                  : IS_ADMIN = os.getuid()                    == 0
except AttributeError: IS_ADMIN = windll.shell32.IsUserAnAdmin() != 0

#######################################################################################
# Encoding
#######################################################################################
ENCODING            = 'utf-8'
POTENTIAL_ENCODINGS = [ 'utf-8-sig', 'utf-16', 'cp949', 'euc-kr' ]

#######################################################################################
# Language
#######################################################################################
LANGUAGE = 'ko-KR'

#######################################################################################
# Debug Mode
#######################################################################################
DEBUG_MODE = False

#######################################################################################
# Socket
#######################################################################################
SOCKET_TIMEOUT        = 1.0     # Timeout for one socket (for settimeout)
SOCKET_SEND_TIMEOUT   = 60.0    # Maximum interval between packet transmission
SOCKET_RECV_BUFF_SIZE = 65535   # Maximum buffer size received at one recv()

#######################################################################################
# Raw Socket
#######################################################################################
ICMP_WAIT_TIMEOUT = 2.0         # Maximum waiting time after sending all icmp packets


#######################################################################################
# Pcap
#######################################################################################
PCAP_SEND_TIMEOUT = 60.0        # Maximum interval between packet transmission
PCAP_WAIT_TIMEOUT = 3.0         # Maximum waiting time after sending all packets

#######################################################################################
# Network Scan
#######################################################################################
REGISTER_ONLY_NEW_IP   = True
GUESS_OS_WITH_TTL      = True
GET_HOSTNAME_WITH_NBNS = True

#######################################################################################
# Port Scan
#######################################################################################
PORT_SCAN_RESULT_EXCLUSION_PORTS = ''

#######################################################################################
# Service Scan
#######################################################################################
BANNER                      = ''
SERVICE_SCAN_TIMEOUT        = 0.1
SHOW_PROGRESS_SEND_INTERVAL = 2.0 # seconds
DST_PORT                    = (
    '1,5,7,9,11,13,15,17-25,37,42-43,47,49,51-54,56,58,61,67-74,79-83,88,'
    '90,95,101-102,104-105,107-111,113,115,117-119,123,126,135,137-139,'
    '143,152-153,156,158,161-162,170,177,179,194,199,201,209-210,213,218,'
    '220,225-241,249-255,259,262,264,280,300,308,311,318-320,350-351,356,'
    '366,369-371,383-384,387-389,399,401,427,433-434,443-445,464-465,475,'
    '491,497,500,502,504,510,512-515,517-518,520-521,524-525,530,532-533,'
    '540,542-544,546-548,550,554,556,560-561,563-564,585,587,591,593,601,'
    '604,623,625,631,635-636,639,641,643,646-648,651,653-655,657,660,666,'
    '674,688,690-691,694-695,698,700-702,706,711-712,749-754,760,782-783,'
    '800,802,808,829-833,843,847-848,853,860-862,873,888,897-898,902-903,'
    '953,981,987,989-995,1010-1020,' # 259 ports(https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers) + 1 port(24) = 260 ports
    '1433,'                          # MSSQL
    '1521,'                          # Oracle
    '1523,'                          # Cubrid
    '1526,'                          # Informix
    '2638,'                          # Sybase
    '3260,'                          # iSCSI
    '3306,'                          # MySQL, MariaDB
    '3389,'                          # MS-RDP
    '3690,'                          # SVN
    '5432,'                          # PostgreSQL
    '5900,'                          # VNC
    '6379,'                          # Redis
    '8008,8080,'                     # HTTP
    '8629,'                          # Tibero
    '20300,'                         # Altibase
    '27017,'                         # MongoDB
    '50000'                          # DB2
)

#######################################################################################
# Process
#######################################################################################
POPEN_TIMEOUT         = 300 # seconds

SSH_ENCODING          = 'utf-8'
SSH_CONN_TIMEOUT      = 1.0
SSH_EXEC_TIMEOUT      = 1.0
SSH_COMMAND_WAIT_TIME = 1.0
SSH_BANNER_WAIT_TIME  = 1.0

#######################################################################################
# EXITCODE
#######################################################################################
SUCCESS  = 0
INFO     = 1
WARNING  = 2
FAIL     = 3
ERROR    = 4
REJECTED = 5
REDIRECT = 6
ABORTED  = 7
DEBUG    = 9

EXITCODE = {
      SUCCESS  : 'SUCCESS'
    , INFO     : 'INFO'
    , WARNING  : 'WARNING'
    , FAIL     : 'FAIL'
    , ERROR    : 'ERROR'
    , REJECTED : 'REJECTED'
    , REDIRECT : 'REDIRECT'
    , ABORTED  : 'ABORTED'
    , DEBUG    : 'DEBUG'
}